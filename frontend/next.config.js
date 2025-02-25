/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  typescript: {
    ignoreBuildErrors: false, // Change to true if you want to ignore TypeScript errors in production
  },
};

module.exports = nextConfig;
