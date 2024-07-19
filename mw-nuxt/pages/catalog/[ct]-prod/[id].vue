<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()


  const { data: prod } = await useFetch(`${ config.public.baseURL }/c/prod/${route.params.id}/`)

  const largeImage = ref('')

  onMounted(() => {
    if (prod.value.images.length > 0) {
      largeImage.value = prod.value.images[0].image
    }
  })

</script>



<template>
  <div class="grid grid-cols-1 gap-4 py-4">



    <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
      <div class="flex gap-2">
        <nuxt-link to="/" class="text-white">Главная</nuxt-link>
        <span class="text-white font-semibold">/</span>
        <nuxt-link to="/catalog" class="text-white">Каталог</nuxt-link>
        <span class="text-white font-semibold">/</span>
        <nuxt-link to="/catalog" class="text-white">Сварочные горелки</nuxt-link>
        <span class="text-white font-semibold">/</span>
        <nuxt-link to="/catalog" class="text-white">Сварочные горелки серии SGL</nuxt-link>
        <span class="text-white font-semibold">/</span>
        <nuxt-link to="/catalog" class="text-white">{{ prod.name }}</nuxt-link>
      </div>
    </div>



    <div class="">

      <div class="grid grid-cols-1 gap-4">



        <div class="flex gap-4">

          <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
            <div class="w-[440px] h-[440px] bg-gray-50/0">
              <div class="flex items-center justify-center h-full">
                <img :src="largeImage" />
              </div>
              
            </div>
          </div>

          <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl w-full">
            <div class="grid grid-cols-1 gap-4">
              
              <h1 class="text-white text-2xl">{{ prod.name }}</h1>            
              <div class="text-white" v-html="prod.description"></div>

            </div>

          </div>

        </div>


        <div class="bg-gray-800/0 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
          <div class="flex flex-wrap gap-8 items-center justify-start">
            <div v-for="img in prod.images" :key="img.id">
              
              <div class="">
                <div class="w-[140px] h-[140px] bg-gray-50/0 overflow-hidden">
                  <div class="flex items-center justify-center h-full">
                    <img @click="largeImage = img.image" :src="img.image" class="bg-red-500/0"/>
                  </div>
                </div>
              </div>
              
            </div>
          </div>          
        </div>



      </div>
      


      

    </div>



  </div>
</template>