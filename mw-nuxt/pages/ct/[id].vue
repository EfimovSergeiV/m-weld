<script setup>
  import data from '~/data/ct.json'


</script>



<template>

  <div class="min-h-screen py-4">

    <div class="grid grid-cols-1 gap-4">

      <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
        <div class="grid grid-cols-1 gap-2">
          <p class="text-gray-100 uppercase font-semibold">Каталог продукции</p>
          <div class="flex flex-wrap md:flex-row gap-2 md:gap-8">
            <nuxt-link :to="{ name: 'about' }" class="text-sm md:text-base text-gray-100 ">Главная</nuxt-link>
            <p class="text-sm md:text-base text-gray-100 ">Сварочные горелки</p>
          </div>
        </div>        
      </div>


      <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">

        <div class="flex flex-wrap gap-x-8 gap-y-2">
          <div v-for="sct in data.categories[0].items" class="">
            <nuxt-link :to="{ name: 'ct-id', params: { id: 4 }}" class="text-lg text-white">{{ sct }}</nuxt-link>
          </div>
        </div>


      </div>


      
      
      
      <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
        <p class="text-gray-100 font-semibold text-2xl">Сварочные горелки для аргоно-дуговой сварки</p>

        <div class="">


          
        </div>

      </div>



    </div>



  </div>

</template>