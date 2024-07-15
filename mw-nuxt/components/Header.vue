<script setup>


  const menuVisible = ref(false)

</script>


<template>
  <div>

    <div class="grid grid-cols-1 gap-4">
      <div class="bg-gray-800/50 backdrop-blur-md border-b border-x border-gray-500 px-8 py-4 rounded-b-xl">
        
        <div class="flex items-center justify-between gap-8">
          <div class="grid grid-cols-1 gap-1">
            <nuxt-link :to="{ name: 'index' }" class="text-3xl text-white uppercase font-semibold">m-weld</nuxt-link>
            <p class="text-base text-gray-100 uppercase">Сварочные материалы и комплектующие</p>      
          </div>
          
          <div class="grid grid-cols-1 gap-0.5">
            <p class="text-2xl text-white uppercase font-semibold text-right">+7 (8112) 72-52-13</p>
            <p class="text-sm text-gray-100 uppercase text-right">Контактная информация</p>      
          </div>

        </div>

        <div class="mt-8">
          <div class="flex flex-wrap md:flex-row gap-2 md:gap-8">
            <!-- <button @click="menuVisible = !menuVisible" class="text-sm md:text-base text-gray-100 ">Продукция</button> -->
            <nuxt-link :to="{ name: 'about' }" class="text-sm md:text-base text-gray-100 ">О компании</nuxt-link>
            <p class="text-sm md:text-base text-gray-100 ">Вопросы и ответы</p>
            <p class="text-sm md:text-base text-gray-100 ">Видео</p>
            <p class="text-sm md:text-base text-gray-100 ">Контакты</p>
          </div>
        </div>

      </div>

      <transition name="down-menu">
        <div v-if="menuVisible" class="">
          <div class="bg-gray-800/50 backdrop-blur-md border border-gray-500 px-8 py-4 rounded-xl">

            <div class="flex flex-wrap gap-y-6 gap-x-8">
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Сварочные горелки</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p class="text-sm text-gray-100">Сварочные горелки серии SGL</p>
                    <p class="text-sm text-gray-100">Сварочная горелка без евроразъема</p>
                    <p class="text-sm text-gray-100">Сварочные горелки для аргоно-дуговой сварки</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Комплектующие для сварочных горелок</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p v-for="q in ['Каналы', 'Сопла', 'Наконечники', 'TIG', 'Держатель наконечника', 'Газовый диффузор']" :key="q" class="text-sm text-gray-100">{{ q }}</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Комплектующие</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p v-for="w in ['Центральный адаптер', 'Диодные мосты', 'Кабельные разъемы', 'Центробежные насосы для систем охлаждения', 'Блоки автономного охлаждения', 'Механизмы подачи проволоки' ]" class="text-sm text-gray-100">{{ w }}</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Сварочные аппараты</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p v-for="e in ['ФОРСАЖ', 'ПУРМ', 'ESAB', 'ПДГ', 'HYPERTHERM', 'M-WELD' ]" class="text-sm text-gray-100">{{ e }}</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Cредства индивидуальной защиты и аксессуары</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p v-for="r in ['Сварочные маски и очки','Электрододержатели, клеммы заземления ESAB','Сварочные перчатки ESAB','Инструменты ESAB',]" class="text-sm text-gray-100">{{ r }}</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">ESAB акции и предложения</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p class="text-sm text-gray-100">ROGUE ES 200I PRO</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Упоры</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p class="text-sm text-gray-100">Упоры и кольца</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Проволока</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p v-for="t in ['Порошковая проволока','Сплошная проволока','Медный присадочный материал',]" class="text-sm text-gray-100">{{ t }}</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Сварочные материалы</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p v-for="y in ['Электроды','Флюс','Прутки','Проволока','Порошковая проволока','Проволока для наплавки',]" class="text-sm text-gray-100">{{ y }}</p>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="grid grid-cols-1 gap-0.5">
                  <p class="text-base text-white uppercase font-semibold">Другое</p>
                  <div class="flex flex-wrap gap-y-6 gap-x-8">
                    <p v-for="u in ['Спреи','Антипригарная паста','Антипригарная жидкость','Травильная паста StainClean','Тележки под баллоны','Растворитель-обезжириватель',]" class="text-sm text-gray-100">{{ u }}</p>
                    <p class="text-sm text-gray-100">Сварочная горелка без евроразъема</p>
                    <p class="text-sm text-gray-100">Сварочные горелки для аргоно-дуговой сварки</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>


    </div>

  </div>
</template>