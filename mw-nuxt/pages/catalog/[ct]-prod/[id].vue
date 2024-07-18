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
      <p class="text-white">Сварочные горелки / Сварочные горелки серии SGL /</p>
    </div>



    <div class="">

      <div class="grid grid-cols-1 gap-4">



        <div class="grid grid-cols-2 gap-4">

          <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
            <div class="w-[440px] h-[440px] bg-gray-50/10">
              <div class="flex items-center justify-center h-full">
                <img :src="largeImage" />
              </div>
              
            </div>
          </div>

          <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
            <div class="grid grid-cols-1 gap-4">
              <h1 class="text-white text-2xl">{{ prod.name }}</h1>            
              
              <p class="text-white">{{ prod }}</p>
              <div class="text-white" v-html="prod.description"></div>              
            </div>

          </div>

        </div>


        <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">
          <div class="flex flex-wrap gap-8 items-center justify-start">
            <div v-for="img in prod.images" :key="img.id">
              
              <div class="">
                <div class="w-[140px] h-[140px] bg-gray-50/10 overflow-hidden">
                  <div class="flex items-center justify-center h-full">
                    <img @click="largeImage = img.image" :src="img.image" class="bg-red-500/20"/>
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