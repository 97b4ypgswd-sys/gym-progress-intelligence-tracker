import streamlit as st

st.title("Gym Progress Intelligence Tracker")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=10, max_value=100)
weight = st.number_input("Enter your weight (kg)", min_value=1.0)
height = st.number_input("Enter your height (cm)", min_value=1.0)

goal = st.selectbox(
   "Select Your Goal",
   ["Fat Loss", "Muscle Gain", "Maintenance"]
)

if st.button("Calculate Report"):

   height_m = height / 100
   bmi = weight / (height_m ** 2)

   if bmi < 18.5:
       category = "Underweight"
   elif bmi < 25:
       category = "Normal Weight"
   elif bmi < 30:
       category = "Overweight"
   else:
       category = "Obese"

   protein = weight * 2
   water = weight * 35

   st.subheader("Gym Progress Report")

   st.write("Name:", name)
   st.write("Age:", age)
   st.write("Weight:", weight, "kg")
   st.write("Height:", height, "cm")

   st.write("BMI:", round(bmi, 2))
   st.write("BMI Category:", category)

   st.write("Recommended Protein:", round(protein), "grams/day")
   st.write("Recommended Water:", round(water), "ml/day")

   st.subheader("Goal Recommendation")

   if goal == "Fat Loss":
       st.write("• Stay in a calorie deficit")
       st.write("• Eat high protein foods")
       st.write("• Walk 8,000-10,000 steps daily")
       st.write("• Do strength training 4-5 times per week")

   elif goal == "Muscle Gain":
       st.write("• Stay in a calorie surplus")
       st.write("• Focus on progressive overload")
       st.write("• Eat sufficient protein daily")
       st.write("• Sleep at least 7-8 hours")

   else:
       st.write("• Maintain current calorie intake")
       st.write("• Continue regular workouts")
       st.write("• Stay hydrated")
       st.write("• Monitor body weight weekly")

   strength_score = (weight * 0.6) + (100 - abs(22 - bmi))

   st.subheader("Strength Level")

   if strength_score < 50:
       st.write("Level: Beginner")
   elif strength_score < 70:
       st.write("Level: Intermediate")
   else:
       st.write("Level: Advanced")

   st.success("Report Generated Successfully!")