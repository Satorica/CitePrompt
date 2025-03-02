def clean_file(input_path, output_path):
    with open(input_path, 'rb') as f:
        content = f.read()
    
    decoded_content = content.decode('utf-8', errors='ignore')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(decoded_content)
    
    print(f"已清理文件并保存到 {output_path}")

input_file = "./acl_arc/test/train_xlData.jsonl"
output_file = "./acl_arc/test/train_xlData_cleaned.jsonl"
clean_file(input_file, output_file)