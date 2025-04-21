import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report


train_df = pd.read_csv("NSL_KDD/KDDTrain+.txt", header=None)
test_df = pd.read_csv("NSL_KDD/KDDTest+.txt", header=None)

#Field Names
columns = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root",
    "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate", "label", "difficulty"
]

train_df.columns = columns
test_df.columns = columns

X_train = train_df.drop(["label", "difficulty"], axis=1)
X_test = test_df.drop(["label", "difficulty"], axis=1)

#'normal' və ya 'attack' olaraq sadələşdiririk
train_df['label'] = train_df['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')
test_df['label'] = test_df['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')

#Mətn formatlı sütunları rəqəmlərə çeviririk
categorical_cols = ['protocol_type', 'service', 'flag']
encoder = LabelEncoder()
for col in categorical_cols:
    train_df[col] = encoder.fit_transform(train_df[col])
    test_df[col] = encoder.transform(test_df[col])

#Label və xüsusiyyətləri ayırırıq
X_train = train_df.drop("label", axis=1)
y_train = train_df["label"]
X_test = test_df.drop("label", axis=1)
y_test = test_df["label"]

#Isolation Forest modelini qururuq
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=43)
model.fit(X_train)

#Təxminlər edir
y_pred = model.predict(X_test)

#Nəticələri 'normal' və 'attack' olaraq tərcümə edirik
y_pred = ['normal' if x == 1 else 'attack' for x in y_pred]

#Hesabat çıxarırıq
print(classification_report(y_test, y_pred))
