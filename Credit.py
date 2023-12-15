import numpy as np
import pandas as pd
import lightgbm as lgb
import matplotlib.pyplot as plt
import seaborn as sns
class Credit:
    def __init__(self,*arg):
        features = ['RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30-59DaysPastDueNotWorse',
            'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
            'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfDependents']
        self.user_input={}
        for index,feature in enumerate(features):
            value = arg[index][feature]
            self.user_input[feature] = float(value)
        self.new_input_data = pd.DataFrame([user_input])
        self.advise=""
    def add_advise(self,advise):
        self.advise+=advise
    def advice(self,customer_features,non_zero_features,good_customer_data):

        print("建議 : ")
        if non_zero_features.any().any():
            print(f"保持良好信用，消除不良紀錄")
        if customer_features['MonthlyIncome'].values[0] < good_customer_data['MonthlyIncome'].mean() :
            print(f"建議將月收入提升至 : {good_customer_data['MonthlyIncome'].mean()}以上")
        if customer_features['RevolvingUtilizationOfUnsecuredLines'].values[0] > good_customer_data['RevolvingUtilizationOfUnsecuredLines'].mean() :
            print(f"建議將貸款信用比降低至 : {good_customer_data['RevolvingUtilizationOfUnsecuredLines'].mean()}以下")
        if customer_features['DebtRatio'].values[0] > good_customer_data['DebtRatio'].mean() :
            print(f"建議將月支出收入比降低至 : {good_customer_data['DebtRatio'].mean()}以下")
        if customer_features['NumberOfOpenCreditLinesAndLoans'].values[0] > good_customer_data['NumberOfOpenCreditLinesAndLoans'].mean() :
            print(f"建議將當前信用貸款案件數量降低至 : {good_customer_data['NumberOfOpenCreditLinesAndLoans'].mean()}以下")


    def Draw_good_customer_plt(self,good_customer_data):
    # 設定子圖
        features = ['RevolvingUtilizationOfUnsecuredLines', 'DebtRatio', 'MonthlyIncome','NumberOfOpenCreditLinesAndLoans']

        fig, axes = plt.subplots(nrows=len(features), figsize=(10, 6 * len(features)))

        for idx, feature in enumerate(features):
        # 計算每個特徵的資料數量
            feature_counts = good_customer_data[feature].value_counts()

            # 畫條形圖
            sns.barplot(x=feature_counts.index, y=feature_counts.values, ax=axes[idx])
            axes[idx].set_title(f'Distribution of {feature}')
            axes[idx].set_xlabel(feature)
            axes[idx].set_ylabel('資料數量')

        # 設定 x 軸刻度間隔和標籤
        if feature == 'RevolvingUtilizationOfUnsecuredLines':
            axes[idx].set_xticks(np.arange(0, 1.5, 0.1))
            axes[idx].set_xticklabels([f'{x:.1f}' for x in np.arange(0, 1.5, 0.1)])
        elif feature == 'DebtRatio':
            axes[idx].set_xticks(np.arange(0, 3.1, 0.1))
            axes[idx].set_xticklabels([f'{x:.1f}' for x in np.arange(0, 3.1, 0.1)])
        elif feature == 'MonthlyIncome':
            axes[idx].set_xticks(np.arange(0, 20001, 2000))
            axes[idx].set_xticklabels([f'{x:.0f}' for x in np.arange(0, 20001, 2500)])
        elif feature == 'NumberOfOpenCreditLinesAndLoans':
            axes[idx].set_xticks(np.arange(0, 31, 2))
            axes[idx].set_xticklabels([str(x) for x in np.arange(0, 31, 2)])

        plt.tight_layout()
        plt.show()

    def Draw_plt(self,combined_data):
    # 畫各年齡層的圖
        features_of_interest = ['RevolvingUtilizationOfUnsecuredLines', 'DebtRatio', 'MonthlyIncome','NumberOfOpenCreditLinesAndLoans']

        # 設定子圖
        fig, axes = plt.subplots(nrows=len(features_of_interest), figsize=(10, 6 * len(features_of_interest)))

        # 把20歲以下95歲以上在圖上刪掉
        combined_data_filtered = combined_data[(combined_data['age'] >= 20) & (combined_data['age'] <= 95)]

        # 3個年齡層當一個單位
        combined_data_filtered['AgeGroup'] = (combined_data_filtered['age'] // 3) * 3

        for idx, feature in enumerate(features_of_interest):
            # 計算該年齡層的平均數
            age_grouped_data = combined_data_filtered.groupby('AgeGroup')[feature].median().reset_index()

            # 畫圖
            sns.barplot(x='AgeGroup', y=feature, data=age_grouped_data, ax=axes[idx])
            axes[idx].set_title(f'{feature} vs. AgeGroup')
            axes[idx].set_xlabel('年齡')
            axes[idx].set_ylabel(feature)

        plt.tight_layout()
        plt.show()


    def DebtRatio_rank(self,customer_features,combined_data,same_age_data):
    #月支出收入比排名
        DebtRatio_rank_percentage = (((combined_data['DebtRatio'] < customer_features['DebtRatio'].values[0]).sum() + 1) / len(combined_data)) * 100
        same_age_DebtRatio_rank_percentage = (((same_age_data['DebtRatio'] < customer_features['DebtRatio'].values[0]).sum() + 1) / len(same_age_data)) * 100
        print(f"客戶的月支出收入比排名前: {DebtRatio_rank_percentage} %")
        print(f"客戶在同年齡層的月支出收入比排名前: {same_age_DebtRatio_rank_percentage} %")


    def RevolvingUtilizationOfUnsecuredLines_rank(self,customer_features,combined_data,same_age_data):
    #貸款信用比排名
        RevolvingUtilizationOfUnsecuredLines_rank_percentage = (((combined_data['RevolvingUtilizationOfUnsecuredLines'] < customer_features['RevolvingUtilizationOfUnsecuredLines'].values[0]).sum() + 1) / len(combined_data)) * 100
        same_age_RevolvingUtilizationOfUnsecuredLines_rank_percentage = (((same_age_data['RevolvingUtilizationOfUnsecuredLines'] < customer_features['RevolvingUtilizationOfUnsecuredLines'].values[0]).sum() + 1) / len(same_age_data)) * 100
        print(f"客戶的貸款信用比排名前: {RevolvingUtilizationOfUnsecuredLines_rank_percentage} %")
        print(f"客戶在同年齡層的貸款信用比排名前: {same_age_RevolvingUtilizationOfUnsecuredLines_rank_percentage} %")


    def MonthlyIncome_rank(self,customer_features,combined_data,same_age_data):
    #月收入排名
        MonthlyIncome_rank_percentage = 100 - ((((combined_data['MonthlyIncome'] < customer_features['MonthlyIncome'].values[0]).sum() + 1) / len(combined_data)) * 100)
        same_age_MonthlyIncome_rank_percentage = 100 - ((((same_age_data['MonthlyIncome'] < customer_features['MonthlyIncome'].values[0]).sum() + 1) / len(same_age_data)) * 100)
        print(f"客戶的月收入排名前: {MonthlyIncome_rank_percentage} %")
        print(f"客戶在同年齡層的月收入排名前: {same_age_MonthlyIncome_rank_percentage} %")

    def customer_rank_percentage(self,user_input,threshold):
    # 所有資料
        train_data = pd.read_csv('cs-training.csv')
        test_data = pd.read_csv('cs-test.csv')
        result_data = pd.read_csv('result.csv')

        # 整理資料
        new_input_data = pd.DataFrame([user_input])
        combined_data = pd.concat([train_data, test_data])
        customer_features = pd.DataFrame([user_input],columns=combined_data.columns)
        same_age_data = combined_data[combined_data['age'] == customer_features['age'].values[0]]
        bad_record_feature = ['NumberOfTime30-59DaysPastDueNotWorse', 'NumberOfTimes90DaysLate', 'NumberOfTime60-89DaysPastDueNotWorse']
        non_zero_features = new_input_data[bad_record_feature].apply(lambda x: x != 0)
        good_customer_data = result_data[result_data['Predicted_Probabilities'] < threshold]

        # 各項排名 (呵呵 寫超醜)
        RevolvingUtilizationOfUnsecuredLines_rank(customer_features,combined_data,same_age_data)
        DebtRatio_rank(customer_features,combined_data,same_age_data)
        MonthlyIncome_rank(customer_features,combined_data,same_age_data)


    # 列出不良紀錄
        if non_zero_features.any().any():
            print("不良紀錄:")
            for feature in bad_record_feature:
                if non_zero_features[feature].values[0]:
                    print(f"{feature}: {int(user_input[feature])}")
        else:
            print("無不良紀錄")

        # 改進建議
        advice(customer_features,non_zero_features,good_customer_data)

        # 畫各年齡層的圖
        Draw_plt(combined_data)

        # 畫優良用戶的圖
        Draw_good_customer_plt(good_customer_data)

# 把model load進來
model = lgb.Booster(model_file='iot_lightgbm_model.txt')

# 特徵

features = ['RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30-59DaysPastDueNotWorse',
            'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
            'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse', 'NumberOfDependents']

# 使用者輸入
user_input = {}
for feature in features:
    value = input(f"請輸入 {feature}: ")
    user_input[feature] = float(value)  # Assuming the input is numeric, adjust if needed

# 把使用者輸入的資料整理成DataFrame
new_input_data = pd.DataFrame([user_input])





# 預測使用者90天會欠款之機率
predictions = model.predict(new_input_data[features], num_iteration=model.best_iteration)
print(f"預測結果 = {predictions[0]}")

# 設定最佳閾值
threshold = 0.07403868112923592

if predictions[0]<threshold :
  print(f"建議給此客戶貸款之金額 : {user_input['MonthlyIncome']*15*(1-predictions[0])} ~ {user_input['MonthlyIncome']*22*(1-predictions[0])}")
  customer_rank_percentage(user_input,threshold)
else :
  print('不建議借貸給此用戶')
  customer_rank_percentage(user_input,threshold)
