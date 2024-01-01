import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# 读取Excel文件
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# 提取特征和标签
X = df.iloc[:, 1:5]  # 第2-5列作为特征
y = df.iloc[:, 7]    # 第8列作为预测结果

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化XGBoost分类器
model = XGBClassifier()

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy}")