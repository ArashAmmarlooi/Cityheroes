"use client";

import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useQuery } from "@tanstack/react-query";
import { setUsers } from "../../redux/slices/userSLice";
import { RootState } from "../../redux/store/store";
import styles from "./users.module.scss";

// Define User Type
interface User {
  id: number;
  username: string;
  email: string;
  location: string;
  availability: boolean;
  reviews: number;
  profile_picture: string;
}

// Fetch Users Using React Query
const fetchUsers = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/users/");
  return res.json();
};

export default function UsersList({ users }: { users: User[] }) {
  const dispatch = useDispatch();
  const reduxUsers = useSelector((state: RootState) => state.users.users);

  // Fetch users with React Query
  const { data, isLoading } = useQuery({
    queryKey: ["users"],
    queryFn: fetchUsers,
    initialData: users, // ✅ Use server-fetched data first
  });

  useEffect(() => {
    if (data) dispatch(setUsers(data)); // ✅ Store fetched users in Redux
  }, [dispatch, data]);

  if (isLoading) return <p>Loading users...</p>;

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>Users</h1>
      <div className={styles.usersList}>
        {reduxUsers.map((user) => (
          <div key={user.id} className={styles.userCard}>
            <img
              src={user.profile_picture}
              alt={user.username}
              className={styles.userImage}
            />
            <div className={styles.userInfo}>
              <h2>{user.username}</h2>
              <p className={styles.location}>{user.location}</p>
              <p className={styles.availability}>
                {user.availability ? "Available ✅" : "Not Available ❌"}
              </p>
              <div className={styles.reviews}>
                {[...Array(5)].map((_, index) => (
                  <span
                    key={index}
                    className={
                      index < user.reviews
                        ? styles.filledStar
                        : styles.emptyStar
                    }
                  >
                    ★
                  </span>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
