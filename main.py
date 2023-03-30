import streamlit as st
import openai


# 设置 OpenAI API 密钥
openai.api_key = st.secrets["GPTKey"]

# 创建一个函数，使用 OpenAI 的 GPT-3.5 模型生成一份简历
def generate_resume(personal_info, resume_description):
    prompt = f"生成一份简历：\n\n个人信息：{personal_info}\n\n履历描述：{resume_description}\n\n生成的简历："
    response = openai.Completion.create(
      engine="davinci", prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5,
    )
    resume = response.choices[0].text.strip()
    return resume

# 创建 Streamlit 应用程序
def main():
    st.title("简历生成器")

    # 创建表单，允许用户输入个人信息和履历描述
    st.subheader("请输入您的个人信息和履历描述")
    name = st.text_input("姓名")
    email = st.text_input("邮箱")
    phone = st.text_input("联系电话")
    education = st.text_input("教育经历")
    experience = st.text_area("工作经历")

    # 当用户提交表单时，生成一份简历
    if st.button("生成简历"):
        personal_info = f"{name}\n{email}\n{phone}\n{education}"
        resume = generate_resume(personal_info, experience)
        st.subheader("生成的简历")
        st.write(resume)

if __name__ == "__main__":
    main()
