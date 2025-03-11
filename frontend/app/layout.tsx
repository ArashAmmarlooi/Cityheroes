"use client";

import React from "react";
import NavBar from "../component/navbar";
import "../styles/globals.scss";
import { wrapper } from "../redux/store/store";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { useRouter } from "next/navigation"; // ✅ Import useRouter properly

const queryClient = new QueryClient();

function RootLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter(); // ✅ Ensures router is available

  return (
    <QueryClientProvider client={queryClient}>
      <div>
        <NavBar />
        {children}
      </div>
    </QueryClientProvider>
  );
}

export default RootLayout;
