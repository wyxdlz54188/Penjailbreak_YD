   import sys
   import hashlib

   def calculate_md5(file_path, start, end):
      hasher = hashlib.md5()
      with open(file_path, 'rb') as f:
         f.seek(start)
         while start < end:
               buffer = f.read(min(1024 * 1024, end - start))  # 每次读取1MB，避免内存占用过高
               if not buffer:
                  break
               hasher.update(buffer)
               start += len(buffer)
      return hasher.hexdigest()

   def main():
      if len(sys.argv) != 2:
         print("Usage: ./md5_splitter.py <file_path>")
         sys.exit(1)

      file_path = sys.argv[1]
      segment_sizes = [
         104857600, 209715200, 314572800, 419430400, 524288000,
         629145600, 734003200, 838860800, 943718400, 1048576000,
         1153433600, 1258291200, 1363148800, 1397088268
      ]  #！！[重要]！！这里修改为你自己的冈易更新请求里"segmentMd5"那一块每一个"endpos\"的数字
      segment_md5s = []

      start = 0
      for end in segment_sizes:
         md5_value = calculate_md5(file_path, start, end)
         segment_md5s.append(md5_value)
         start = end

      # 输出14个MD5值
      for i, md5 in enumerate(segment_md5s, start=1):
         print(f"输出: {md5}")

   if __name__ == "__main__":
      main()
