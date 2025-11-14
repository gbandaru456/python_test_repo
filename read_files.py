import os as os
import pandas as pd
import glob
list_df=[]
target_path="C:/Users/gbandaru/python_new_project/target/stack_output.csv"
target_path_gz="C:/Users/gbandaru/python_new_project/target/stack_output.csv.gz"
all_files=glob.glob("C:/Users/gbandaru/python_new_project/source/*.csv")
source="C:/Users/gbandaru/python_new_project/source/"
for files in all_files:
    df=pd.read_csv(files)
    df['File_name']=os.path.basename(files)
    list_df.append(df)
    df_new=pd.concat(list_df,axis=0,ignore_index=True)
    df_new.to_csv(target_path,sep=",",index=False)
    df_new.to_csv(target_path_gz,index=False,compression='gzip')
