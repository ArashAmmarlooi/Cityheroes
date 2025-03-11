"use client";
import { useRouter } from "next/navigation";
import { useState } from "react";
import styles from "./login.module.scss";
import Link from "next/link";

export default function Login(): JSX.Element {
  const router = useRouter();
  const [loginMethod, setLoginMethod] = useState<"email" | "phone">("email");
  const [isOtpSent, setIsOtpSent] = useState(false);

  const handleSendOTP = () => {
    setIsOtpSent(true);
  };

  return (
    <div className={styles.container}>
      <div className={styles.leftSection}>
        <h1>Welcome Back!</h1>
        <p>Login to continue</p>
      </div>

      <div className={styles.rightSection}>
        <h2>
          {loginMethod === "email" ? "Login with Email" : "Login with Phone"}
        </h2>

        {loginMethod === "email" ? (
          <>
            <input type="email" placeholder="Email" />
            <input type="password" placeholder="Password" />
            <button className={styles.loginButton}>Login</button>
          </>
        ) : (
          <>
            {!isOtpSent ? (
              <>
                <input type="text" placeholder="Mobile Number" />
                <button className={styles.otpButton} onClick={handleSendOTP}>
                  Send OTP
                </button>
              </>
            ) : (
              <>
                <input type="text" placeholder="Enter OTP" />
                <button className={styles.loginButton}>Verify & Login</button>
              </>
            )}
          </>
        )}

        <div className={styles.options}>
          <p>
            Don't have an account?{" "}
            <Link href="/register">
              <span className={styles.link}>Register</span>
            </Link>
          </p>
          <p
            className={styles.switchText}
            onClick={() =>
              setLoginMethod(loginMethod === "email" ? "phone" : "email")
            }
          >
            {loginMethod === "email"
              ? "Login with Phone?"
              : "Login with Email?"}
          </p>
        </div>
      </div>
    </div>
  );
}
