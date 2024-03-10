# Mengimpor library dan membaca data dari file csv
import pandas as pd
stress = pd.read_csv('SaYoPillow.csv')

# Melihat informasi dalam dataset
stress.info()

# Menampilkan 10 baris pertama
stress.head(10)

# Memisahkan atribut dengan label, yang dimana x adalah atribut dan y adalah label
X = stress[['sr', 'rr', 't', 'lm', 'bo', 'rem', 'sr.1', 'hr']]
y = stress['sl']


# Membagi dataset menjadi data latih dan data uji
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=123)

# Evaluasi model
from sklearn.metrics import accuracy_score
y_pred =  tree_model.predict(X_test)
accuracy_score =round(accuracy_score(y_pred, y_test), 3)
print('Accuracy: ',accuracy_score)

# Prediksi model
# Menggunakan decision tree model yang sdh dibuat dengan variabel (['sr', 'rr', 't', 'lm', 'bo', 'rem', 'sr.1', 'hr'])
print(tree_model.predict([[93.00, 25.00, 91.00, 16.00, 89.00, 99.00, 1.00, 74.00]])[0])

# Prediksi model
print(tree_model.predict([[55.00, 19.00, 95.00, 9.00, 94.00, 82.00, 6.00, 57.00]])[0])

# Melihat class names
print(tree_model.classes_)

#Melihat visualisasi data decision tree
from sklearn.tree import export_graphviz

#Menentukan nama kelas sesuai dengan yang digunakan dalam model
class_names = [str(cls) for cls in tree_model.classes_]

export_graphviz(
    tree_model,
    out_file="stress_tree.dot",
    feature_names=['sr', 'rr', 't', 'lm', 'bo', 'rem', 'sr.1', 'hr'],
    class_names=['0', '1', '2', '3', '4'],
    rounded=True,
    filled=True
)