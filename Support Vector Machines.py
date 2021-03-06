import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
print(digits.data)
print(digits.target)
clf = svm.SVC()
clf = svm.SVC(gamma = 0.001,C=100)
x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)
print(clf.predict(digits.data[-5]))
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
