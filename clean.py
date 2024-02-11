import argparse
import pandas as pd

def clean_data(input1, input2, output):
    # 读取输入文件
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    # 合并两个输入文件，并删除冗余的列
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    merged_df = merged_df.drop('id', axis=1)

    # 删除含有缺失值的行
    merged_df = merged_df.dropna()

    # 删除职位中包含'insurance'或'Insurance'的行
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    # 保存清洗后的数据
    merged_df.to_csv(output, index=False)
    # Print the shape of the output file


if __name__ == "__main__":
    # 创建解析器对象
    parser = argparse.ArgumentParser()

    # 添加位置参数
    parser.add_argument('input1', help='input1（csv）')
    parser.add_argument('input2', help='input2（csv）')
    parser.add_argument('output', help='output（csv）')

    # 解析命令行参数
    args = parser.parse_args()

    # 执行数据清洗
    clean_data(args.input1, args.input2, args.output)