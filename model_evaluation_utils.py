from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


def evaluate_model(y_true, y_pred, labels, title="Confusion Matrix"):
    print("✅ Accuracy:", accuracy_score(y_true, y_pred))
    print("\n📊 Classification Report:\n", classification_report(
        y_true, y_pred, target_names=labels))

    cm = confusion_matrix(y_true, y_pred)
    ConfusionMatrixDisplay(confusion_matrix=cm,
                           display_labels=labels).plot(cmap='Blues')

    plt.title(title)
    plt.show()


# --- Solo Mode Test Block ---
if __name__ == "__main__":
    # Example ground truth and predictions
    y_true = [0, 1, 1, 0, 1, 0]
    y_pred = [0, 1, 0, 0, 1, 1]
    labels = ["Class 0", "Class 1"]

    evaluate_model(y_true, y_pred, labels, title="Test Confusion Matrix")
