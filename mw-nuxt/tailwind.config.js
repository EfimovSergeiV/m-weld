/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.vue",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      screens: {
        sm: '520px',
        md: '820px',
        lg: '1140px',
        xl: '1440px',
      },
      container: {
        center: true,
      },
      colors: {
        'main-primary': '#074866',
        'main-secondary': '#0F293E',
        'main-dark': '#001E35',
        'main-info': '#2A72A9',
        'main-light': '#4C80A9',
      },
      fontFamily: {
        'sans': ['Play', 'Noto Sans', 'Open Sans', ],
      },
    },
  },
}