<script setup>


  const menuVisible = ref(false)

</script>


<template>
  <div>

    <div class="grid grid-cols-1 gap-4">
      <div class="bg-gray-800/50 backdrop-blur-md border-b border-x border-gray-500 px-8 py-4 rounded-b-xl">
        
        <div class="flex items-center justify-between gap-8">
          <div class="grid grid-cols-1 gap-1">
            <nuxt-link :to="{ name: 'index' }" class="text-4xl text-white uppercase font-semibold">m-weld</nuxt-link>
            <p class="text-sm text-gray-100 uppercase">Сварочные материалы и комплектующие</p>      
          </div>
          
          <div class="grid grid-cols-1 gap-0.5">
            <p class="text-2xl text-white uppercase font-semibold text-right">+7 (8112) 72-52-13</p>
            <p class="text-sm text-gray-100 uppercase text-right">Контактная информация</p>      
          </div>

        </div>



      </div>

      <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
        <div class="">
          <div class="flex flex-wrap md:flex-row gap-2 md:gap-8">
            <nuxt-link :to="{ name: 'about' }" class="text-sm md:text-base text-gray-100 ">О компании</nuxt-link>
            <p class="text-sm md:text-base text-gray-100 ">Вопросы и ответы</p>
            <p class="text-sm md:text-base text-gray-100 ">Видео</p>
            <p class="text-sm md:text-base text-gray-100 ">Контакты</p>
          </div>
        </div>        
      </div>


    </div>

  </div>
</template>