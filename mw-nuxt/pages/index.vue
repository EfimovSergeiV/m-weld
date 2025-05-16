<script setup>
  const config = useRuntimeConfig()


  const { data: cts } = await useFetch(`${ config.public.baseURL }/c/cts/`)


</script>


<template>
  <div class="container px-4 mx-auto">
    <div class="flex gap-24 py-4">

      <div class="w-full">
        <div class="grid grid-cols-1 gap-4">

          <div class="py-6">
            <div class="">
              <div class="grid grid-cols-1 gap-4">
                <p class="text-2xl text-white uppercase font-semibold">О нас</p>
                <p class="text-base text-gray-100">
                  Компания ООО «Техносвар КС» была основана в 2005 году, и на сегодняшний день является одной из ведущих и динамично развивающихся компаний на Северо-Западе России.
                  Основным направлениями нашей деятельности является поставка сварочных материалов и аксессуаров для сварочных работ.
                  Мы предлагаем широкий ассортимент сварочных материалов и аксессуаров для сварки, используемых как в промышленности, так и быту.
                  Компания ООО «Техносвар КС» является официальным дистрибьютором «ESAB» (www.esab.ru), а также является авторизованным сервисным центром продукции «ESAB».
                </p>      
              </div>
            </div>
          </div>


          <div class="">
            <div class="">
              <div class="grid grid-cols-1 gap-0.5">
                <p class="text-2xl text-white uppercase font-semibold">Каталог продукции</p>
                
                <div class="grid grid-cols-4 gap-4 py-4">
                  <div v-for="i in 8" :key="i" class="">
                    
                    <div class="">
                      
                      <div class="bg-white">
                        <div class="grid grid-cols-1 gap-1">
                          <img src="https://m-weld.ru/images/1464874292.jpg" class="py-2 px-2" alt="">
                          <div class="flex items-center justify-center">
                            <nuxt-link :to="{ name: 'catalog-ct', params: { ct: 4 }}" class="text-base text-gray-800 py-2">Ресанта саипа 200</nuxt-link>
                          </div>
                        </div>
                        
                      </div>
                    </div>

                    
                  </div>

                </div>
                
              </div>
            </div>
          </div>



          </div>
      </div>
      <div class="w-[460px] py-6">
        <div class="grid grid-cols-1 gap-4">
          <div class="">
            <div class="">
              <div class="grid grid-cols-1 gap-4">
                
                <p class="text-base text-white uppercase font-semibold">Являемся официальным дистрибьютером компании ESAB</p>
                
                <p class="text-sm text-gray-100">Бренд ESAB - синоним передового опыта в таких областях как: оборудование для ручной сварки и резки, сварочные материалы, автоматизированная сварка, механические системы резки. В каждой из этих сфер ESAB использует постоянно совершенствуемые методы, материалы и ноу-хау, чтобы в полной мере удовлетворить потребности всех секторов промышленности. Компания ЭСАБ разрабатывает высокопроизводительные решения, которые отвечают требованиям заказчиков из всех сегментов рынка и даже превосходят их. ЭСАБ предлагает широкий ассортимент решений практически для любого технологического процесса в области сварки и резки, а также почти для всех сфер применения.</p>      
                
                <div class="">
                  <img src="/esab.png" class="rounded-b-xl" />
                </div>              
              
              </div>

            </div>
          </div>
          <div class="">

          </div>        
        </div>

      </div>

    </div>
  </div>

</template>