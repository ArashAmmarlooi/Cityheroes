import UsersList from "../../component/userList/userList";

async function fetchUsers() {
  const res = await fetch("http://127.0.0.1:8000/api/users/", {
    cache: "no-store",
  });
  return res.json();
}

export default async function UsersPage() {
  const users = await fetchUsers(); // ✅ Fetch users from Django

  return <UsersList users={users} />; // ✅ Send to Client Component
}
