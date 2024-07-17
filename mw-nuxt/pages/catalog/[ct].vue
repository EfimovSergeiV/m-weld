<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()

  console.log(route.params)

  const { data: cts } = await useFetch(`${ config.public.baseURL }/c/cts/${route.params.ct}/`)
  const { data: prods } = await useFetch(`${ config.public.baseURL }/c/prods/${route.params.ct}/`)

</script>



<template>

  <div class="min-h-screen py-4">

    <div class="grid grid-cols-1 gap-4">

      <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
        <div class="grid grid-cols-1 gap-6">
          <p class="text-gray-100 uppercase font-semibold">Каталог продукции</p>
          <div class="flex flex-wrap md:flex-row gap-2 md:gap-8">
            <nuxt-link :to="{ name: 'about' }" class="text-sm md:text-base text-gray-100 ">Главная</nuxt-link>
            <p class="text-sm md:text-base text-gray-100 ">Сварочные горелки</p>
          </div>
          <p class="text-gray-100 font-semibold text-2xl">Сварочные горелки для аргоно-дуговой сварки</p>
        </div>        
      </div>


      <div v-if="cts.length > 0" class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
        <div class="flex flex-wrap gap-x-8 gap-y-2">
          <div v-for="sct in cts" class="">
            <nuxt-link :to="{ name: 'catalog-ct', params: { ct: sct.id }}" class="text-lg text-white">{{ sct.name }}</nuxt-link>
          </div>
        </div>
      </div>


      
      
      
      <div class="">
        <div class="grid grid-cols-1 gap-8">
          <!-- <p class="text-gray-100 font-semibold text-2xl">Сварочные горелки для аргоно-дуговой сварки</p> -->

          <div class="grid grid-cols-4 gap-4">

            <div v-for="prod in prods" :key="prod.id" class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
              <div class="grid grid-cols-1 gap-4">
                <div class="flex items-center justify-center">
                  <img :src="prod.preview" />
                </div>
                <div class="flex items-center justify-center">
                  <p class="text-white text-center">{{ prod.name }}</p>
                </div>
              </div>
            </div>

          </div>          
        </div>


      </div>



    </div>



  </div>

</template>