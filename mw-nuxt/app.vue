<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtLayout>
      <NuxtLoadingIndicator :color="'repeating-linear-gradient(to right,#f97316 0% ,#f97316 100%)'" :height="2" />
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
