import re


def process_data(input_file, output_file):
    # 读取输入文件的所有行
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        # 1. 提取trigger, replacement, options字段
        trigger_match = re.search(r'trigger: "(.*?)"', line)
        replacement_match = re.search(r'replacement: "(.*?)"', line)
        options_match = re.search(r'options: "(.*?)"', line)

        if not (trigger_match and replacement_match and options_match):
            processed_lines.append(line.strip())  # 无法解析的行保持原样
            continue

        trigger = trigger_match.group(1)
        replacement = replacement_match.group(1)
        options = options_match.group(1)

        # 2. 步骤1: 将所有反斜杠变成双倍 (只处理replacement部分)
        replacement = replacement.replace('\\', '\\\\')

        # 3. 步骤2: 如果replacement中没有|，则在末尾添加|
        if '|' not in replacement:
            replacement += '|'

        # 4. 新要求: 只对mA行的trigger进行反斜杠翻倍处理
        if options == 'mA':
            trigger = trigger.replace('\\', '\\\\')

        # 5. 步骤3 & 4: 根据选项类型处理
        if options == 'rmA':
            # 步骤3: 处理rmA类型
            new_line = f'    [\n        "r/{trigger}/|",\n        "{replacement}"\n    ],'
        elif options == 'mA':
            # 步骤4: 处理mA类型
            new_line = f'    [\n        "{trigger}|",\n        "{replacement}"\n    ],'
        else:
            new_line = line.strip()  # 未知选项保持原样

        processed_lines.append(new_line)

    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(processed_lines))


# 使用示例
process_data('data_input.json', 'data_output.json')