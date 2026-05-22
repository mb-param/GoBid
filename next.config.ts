import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  turbopack: {
    /** Monorepo: lockfiles exist above tender-platform — pin Turbopack root to this app. */
    root: __dirname,
  },
};

export default nextConfig;
