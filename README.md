# iris-classification

Classification of Irsi data is a well known benchmark problem in machine learning research.
This data set is downloadable from ftp.ics.uci.edu/pub/machine-learning-databases.The
problem in Iris data is to classify three species of iris (setosa, versicolor and virginica) by
four-dimensional attribute vectors consisting of sepal length (x1), sepal width (x2), petal length
(x3) and petal width (x4). There are 50 samples of each class in this data set.
We now consider a fuzzy classifier with a set of fuzzy rules to classify Iris data. The values
of attributes are normalized before fuzzy processing.
Every attribute of the fuzzy classifier is assigned with three linguistic terms
(fuzzy sets): short, middle and long.
Further we suppose that the following set of fuzzy rules have been defined by experts to
classify iris data.
r1: If (x1=short 􀂛 long) and (x2=middle 􀂛 long) and (x3=middle 􀂛 long ) and (x4=middle)
Then iris versicolor
r2: If (x3=short 􀂛 middle) and (x4=short) Then iris setosa
r3: If (x2=short 􀂛 middle) and (x3=long) and (x4=long) Then iris virginica
r4: If (x1=middle) and (x2=short 􀂛 middle) and (x3=short) and (x4=long)
Then iris versicolor

