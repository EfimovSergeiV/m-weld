<script setup>


  const menuVisible = ref(false)

</script>


<template>
  <div class="container px-4 mx-auto">

    <div class="grid grid-cols-1 gap-4">
      
      <div class="">
        <div class="flex items-center justify-between gap-8">
          <div class="grid grid-cols-1 gap-1">
            <nuxt-link :to="{ name: 'index' }" class="text-5xl text-white uppercase font-black">m-weld</nuxt-link>
            <p class="text-xs text-gray-100 uppercase">Сварочные материалы и комплектующие</p>      
          </div>

          <div class=" flex items-center gap-12">
            <div class="grid grid-cols-1 gap-2">
              <p class="text-2xl text-white uppercase font-semibold text-right">+7 (8112) 72-52-13</p>
              <p class="text-sm text-gray-100 uppercase text-right">sale@m-weld.ru</p>
            </div>
            <div class="py-4">
              <blockquote class="text-xl font-semibold italic text-center text-gray-700 dark:text-gray-300">
                <span class="before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-blue-600 relative inline-block my-2 lg:my-0 px-4 py-0.5">
                  <span class="relative text-white">ГЛАВНЫЙ СВАРЩИК</span>
                </span>
                <p class="mt-0.5 ml-8 text-white"><span class="text-xs">интернет магазин</span> glsvar.ru</p>
              </blockquote>
            </div>
          </div>

        </div>
      </div>

      <div class="py-6">
        <div class="">
          <div class="flex flex-wrap items-center justify-end md:flex-row gap-1">
            <div class="bg-blue-600 rounded-sm px-6 py-0.5"><p class="text-xl text-gray-100 ">Главная</p></div>
            <div class="bg-blue-600 rounded-sm px-6 py-0.5"><p class="text-xl text-gray-100 ">Контакты</p></div>
            <div class="bg-blue-600 rounded-sm px-6 py-0.5"><nuxt-link :to="{ name: 'about' }" class="text-xl text-gray-100 ">О компании</nuxt-link></div>
          </div>
        </div>        
      </div>

    </div>

  </div>
</template>