def check_metrics_classification(model, X, y, y_pred):
  if len(y_pred) == 0:
    y_pred = model.predict(X)
  
  train_acc = accuracy_score(y_test, y_pred_test)
  classification_report_table = classification_report(y_test, y_pred_test)
  
  print('Accuracy:', train_acc)
  print('Classification report:', classification_report_table)

  