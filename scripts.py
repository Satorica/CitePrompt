def clean_file(input_path, output_path):
    # 以二进制模式读取文件
    with open(input_path, 'rb') as f:
        content = f.read()
    
    # 尝试解码，忽略错误
    decoded_content = content.decode('utf-8', errors='ignore')
    
    # 写入新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(decoded_content)
    
    print(f"已清理文件并保存到 {output_path}")

# 使用方法
input_file = "./acl-arc/test/train_xlData.jsonl"
output_file = "./acl-arc/test/train_xlData_cleaned.jsonl"
clean_file(input_file, output_file)