
from classification_regex import classify_with_regex
from classification_bert import classify_with_bert
from classification_llm import classify_with_llm
import pandas as pd

def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels

def classify_log(source, log_message):
  if source=='LegacyCRM':
    label=classify_with_llm(log_message)
  else:
    label=classify_with_regex(log_message)
    if label is None:
      label=classify_with_bert(log_message)
    return label

def classify_csv(input_file):
    df = pd.read_csv(input_file)

    # Perform classification
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    # Save the modified file
    output_file = "output.csv"
    df.to_csv(output_file, index=False)

    return output_file
if __name__ == '__main__':
    classify_csv("Data/test.csv")

