"use client";
import { useState } from "react";
import styles from "./login.module.scss";

export default function Login(): JSX.Element {
  const [isEmailLogin, setIsEmailLogin] = useState<boolean>(true);

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
            {/* Mobile Login */}
            <input type="text" placeholder="Mobile Number" />
            <input type="text" placeholder="OTP Code" />
          </>
        )}

        <button className={styles.loginButton}>Login</button>

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
