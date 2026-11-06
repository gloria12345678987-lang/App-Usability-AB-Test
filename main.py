import pandas as pd
import os

# 1. 基础设置（找路径）
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "app_interface_usability_practice.xlsx")
report_dir = os.path.join(base_dir, "report")

# 确保 report 文件夹存在
os.makedirs(report_dir, exist_ok=True)


# ==========================================
# 抽屉1：数据体检
# ==========================================
def run_eda():
    print("\n" + "=" * 20 + " 1. 开始数据体检 " + "=" * 20)
    df = pd.read_excel(file_path, sheet_name="Raw_Data")

    print("形状:", df.shape)
    print("缺失值:\n", df.isnull().sum())
    print("类别分布:")
    for col in ["interface", "test_order", "task_success"]:
        print(f"\n--- {col} ---")
        print(df[col].value_counts(dropna=False))


# ==========================================
# 抽屉2：数据清洗
# ==========================================
def clean_data():
    print("\n" + "=" * 20 + " 2. 开始数据清洗 " + "=" * 20)
    df = pd.read_excel(file_path, sheet_name="Raw_Data")

    # 填补满意度缺失值
    df['satisfaction_1to7'] = df['satisfaction_1to7'].fillna(df['satisfaction_1to7'].median())

    # 增加一列“成功/失败”文字标签
    df['task_status'] = df['task_success'].map({1: '成功', 0: '失败'})

    print("清洗后，缺失值还剩:", df.isnull().sum().sum(), "个")

    # 保存到 report 文件夹
    output_path = os.path.join(report_dir, "cleaned_data.xlsx")
    df.to_excel(output_path, index=False)
    print(f"✅ 清洗后数据已保存至: {output_path}")


# ==========================================
# 抽屉3：数据分析（暂定，下一步填内容）
# ==========================================
# ==========================================
# 抽屉3：数据分析（正式算账）
# ==========================================
def analyze_data():
    print("\n" + "=" * 20 + " 3. 开始数据分析 " + "=" * 20)

    # 读取刚才洗干净的数据
    output_path = os.path.join(report_dir, "cleaned_data.xlsx")
    df = pd.read_excel(output_path)

    # ----------------------------------------
    # 核心逻辑：过滤出“成功”的数据
    # ----------------------------------------
    # 这句话的意思是：把 df 中 task_success 等于 1 的行，单独抽出来放进 df_success
    df_success = df[df['task_success'] == 1]

    print("总共数据行数:", len(df))
    print("成功任务行数:", len(df_success))
    print("被剔除的失败任务行数:", len(df) - len(df_success))

    # ----------------------------------------
    # 分析1：算成功率 (用完整数据 df)
    # ----------------------------------------
    # groupby('interface') 意思是按 A 和 B 分组
    # task_success 求平均，因为成功是1，失败是0，所以平均值就是成功率！
    success_rate = df.groupby('interface')['task_success'].mean() * 100

    print("\n--- 1. 任务成功率 (%) ---")
    print(success_rate.round(2))  # round(2) 保留两位小数

    # ----------------------------------------
    # 分析2：算平均耗时、错误数、点击次数 (只用成功数据 df_success)
    # ----------------------------------------
    # 关键点：这里用的是 df_success，失败的已经被踢出去了！
    metrics = df_success.groupby('interface')[['task_time_sec', 'error_count', 'click_count']].mean()

    print("\n--- 2. 成功任务的各项平均指标 ---")
    print(metrics.round(2))

    # ----------------------------------------
    # 分析3：算满意度 (用完整数据 df)
    # ----------------------------------------
    satisfaction = df.groupby('interface')['satisfaction_1to7'].mean()
    print("\n--- 3. 平均满意度 ---")
    print(satisfaction.round(2))
# ==========================================
# 总遥控器：想跑哪步，就在这里按哪个按钮
# ==========================================
if __name__ == "__main__":
    # 第一步：体检
    #run_eda()

    # 第二步：清洗
    #clean_data()

    # 第三步：分析
    analyze_data()