"use client";

import React from "react";
import styles from "../styles/page.module.scss";
import Link from "next/link";


export default function Home(): JSX.Element {
  const [search, setSearch] = React.useState<string>("");
  return (
    <main className={styles.container}>
      <h1>Welcome to City Heroes</h1>
      <p>Connecting people who need help with those who can offer it.</p>

      {/* Section that contains Search Bar + Cards */}
      <section className={styles.cardsSection}>
        {/* Search Bar */}
        <div className={styles.searchContainer}>
          <input
            type="text"
            placeholder="Find help..."
            value={search}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
              setSearch(e.target.value)
            }
            className={styles.searchBar}
          />
          <button className={styles.searchButton}>Search</button>
        </div>

        {/* Cards Container */}
        <div className={styles.cardContainer}>
          {/* Card 1: Join as a Helper */}
          <div className={styles.card}>
            <h3>Join as a Helper</h3>
            <p>Offer your skills and assist others in your community.</p>
            <Link href="/login">
              <button>sign up</button>
            </Link>
          </div>

          {/* Card 2: You Help */}
          <div className={styles.card}>
            <h3>You Help</h3>
            <p>Provide services and make a difference in people's lives.</p>
            <button>Start Helping</button>
          </div>
        </div>
      </section>
    </main>
  );
}
