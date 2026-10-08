/** @type {import('next').NextConfig} */
const isGithubPages = process.env.GITHUB_PAGES === 'true' || Boolean(process.env.BASE_PATH);
const basePath = process.env.BASE_PATH || (isGithubPages ? '/main_gd_arena' : '');

const nextConfig = {
  reactStrictMode: true,
  output: 'export',
  basePath: basePath || undefined,
  assetPrefix: basePath ? `${basePath}/` : undefined,
  typescript: {
    ignoreBuildErrors: true,
  },
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: {
    unoptimized: true,
  }
};

export default nextConfig;
