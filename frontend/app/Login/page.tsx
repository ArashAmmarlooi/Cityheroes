"use client";
import { useState, useRef } from "react";
import styles from "./login.module.scss";


export default function Login(): JSX.Element {
  const [isEmailLogin, setIsEmailLogin] = useState<boolean>(true);
  const [phone, setPhone] = useState<string>("");
  const [showOTP, setShowOTP] = useState<boolean>(false);
  const otpInputsRef = useRef<Array<HTMLInputElement | null>>([]);

  const handlePhoneChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPhone(e.target.value);
  };

  const handleOtp = () => {

      setShowOTP(true); // Switch to OTP input when phone number is valid
    
  };

  const handleOTPChange = (index: number, e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value.replace(/\D/, ""); // Allow only digits
    if (value.length > 1) return; // Prevent multiple digits in one box

    if (otpInputsRef.current[index]) {
      otpInputsRef.current[index]!.value = value; // Assign value to input box
    }

    // Move to next input if a digit is entered
    if (value && index < 5) {
      otpInputsRef.current[index + 1]?.focus();
    }
  };

  return (
    <div className={styles.container}>
      {/* Left Section (Blue Background) */}
      <div className={styles.leftSection}>
        <h1>Welcome Back!</h1>
        <p>Login to continue</p>
      </div>

      {/* Right Section (Login Form) */}
      <div className={styles.rightSection}>
        <h2>Login</h2>

        {isEmailLogin ? (
          <>
            {/* Email & Password Login */}
            <input type="email" placeholder="Email" />
            <input type="password" placeholder="Password" />
          </>
        ) : (
          <>
            {/* Phone Input (Hidden when OTP is shown) */}
            {!showOTP ? (
              <input
                type="text"
                placeholder="Mobile Number"
                value={phone}
                onChange={handlePhoneChange}
                maxLength={10}
              />
            ) : (
              <div className={styles.otpContainer}>
                {[...Array(6)].map((_, index) => (
                  <input
                    key={index}
                    type="text"
                    maxLength={1}
                    className={styles.otpInput}
                    onChange={(e) => handleOTPChange(index, e)}
                    ref={(el) => (otpInputsRef.current[index] = el)}
                  />
                ))}
              </div>
            )}
          </>
        )}

        <button onClick={handleOtp} className={styles.loginButton}>
          {!showOTP ? "Login" : "Submit OTP"}
        </button>

        {/* Google Login */}
        <button className={styles.googleButton}>
          <img src="/google-icon.png" alt="Google Logo" />
          Login with Google
        </button>

        {/* Switch between Email & Mobile Login */}
        <p className={styles.switchText}>
          {isEmailLogin ? "Login with Mobile?" : "Login with Email?"}{" "}
          <span onClick={() => setIsEmailLogin(!isEmailLogin)}>Click Here</span>
        </p>
      </div>
    </div>
  );
}
