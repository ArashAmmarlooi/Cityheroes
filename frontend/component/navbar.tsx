import React from "react";
import Image from "next/image";
import Link from "next/link";
import styles from "./navbar.module.scss";

const NavBar: React.FC = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.rightSection}>
        <Link href="/" className={styles.navLink}>
          Home
        </Link>
        <Link href="/requests" className={styles.navLink}>
          Requests
        </Link>
        <Link href="/about" className={styles.navLink}>
          About
        </Link>
      </div>

      <div className={styles.leftSection}>
        <Link href="/">
          <Image
            src="/logo.png"
            alt="City Heroes Logo"
            width={150}
            height={50}
            priority
          />
        </Link>
      </div>
    </nav>
  );
};

export default NavBar;
