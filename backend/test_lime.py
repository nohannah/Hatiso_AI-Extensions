from lime_explainer import explain_prediction

text = "You are a stupid idiot."

print("Generating explanation...")

explanation = explain_prediction(text)

print(explanation)