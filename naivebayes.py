from sklearn.datasets import load_files
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split 
from sklearn import metrics 


F = load_files(tweets.csv)

X = F.data 
y = F.target 
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) 
  
gnb = GaussianNB() 
gnb.fit(X_train, y_train) 
  
y_pred = gnb.predict(X_test) 
  
print("Gaussian Naive Bayes accuracy - ", metrics.accuracy_score(y_test, y_pred)*100, "%")

# Courtesy - GeeksforGeeks