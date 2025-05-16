<script lang="ts" setup>



</script>


<template>
  <div class="">
    <div class="bg-fixed bg-no-repeat bg-center	bg-cover bg-[url('bg/welt.webp')] dark:bg-[url('bg/welt.webp')]">

      <div class=" bg-gradient-to-br from-gray-800/80 via-gray-700/70 to-gray-900/80 backdrop-blur-sm">
        <div class="">
          <div class="min-h-screen grid grid-cols-1 content-between">
            <Header />
            <slot />
            <Footer />
          </div>
        </div>
      </div>

    </div>
  </div>
</template>