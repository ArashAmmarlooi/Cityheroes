"use client";

import React from "react";
import NavBar from "../components/NavBar";
import "../styles/globals.scss";
import { wrapper } from "../store";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <NavBar />
        <QueryClientProvider client={queryClient}>
          {children}
        </QueryClientProvider>
      </body>
    </html>
  );
}

export default wrapper.withRedux(RootLayout);
