import streamlit as st
def main():
    st.title("Temperature Converter")

    # Celsius to Fahrenheit conversion
    celsius = st.number_input("Enter temperature in Celsius:", value=0.0)
    fahrenheit = (celsius * 9/5) + 32
    st.write(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

if __name__ == "__main__":
    main()
