"use client";
import { useRouter } from "next/navigation";
import { useState } from "react";
import styles from "./register.module.scss";
import Link from "next/link";

export default function Register(): JSX.Element {
  const router = useRouter();
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match!");
      return;
    }

    // Handle API request to register user
    console.log("Registering:", formData);
  };

  return (
    <div className={styles.container}>
      <div className={styles.leftSection}>
        <h1>Join Us!</h1>
        <p>Create an account to get started</p>
      </div>

      <div className={styles.rightSection}>
        <h2>Register</h2>

        <form className={styles.form} onSubmit={handleSubmit}>
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="confirmPassword"
            placeholder="Confirm Password"
            value={formData.confirmPassword}
            onChange={handleChange}
            required
          />

          {error && <p className={styles.error}>{error}</p>}

          <button className={styles.registerButton} type="submit">
            Register
          </button>
        </form>

        <p>
          Already have an account?
          <Link href="login">
            <span className={styles.link}>Login</span>
          </Link>
        </p>
      </div>
    </div>
  );
}
