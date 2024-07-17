<script setup>
  const currentData = new Date().getFullYear()

</script>


<template>
  <div>

    <div class="">
      <div class="bg-gray-800/50 backdrop-blur-md border-t border-x border-gray-500 px-8 py-4 rounded-t-xl">
        <div class="flex gap-16 items-start">
          <p class="text-base text-white">© {{ currentData }} Продажа сварочного оборудования	</p>
          <div class="grid grid-cols-1 gap-0.5">
            <p class="text-base text-white">г. Псков, ООО «Техносвар КС», 180006, ул Шоссейная д. 3,</p> 
            <p class="text-base text-white">тел. (8112) 72 52 13, факс: (8112) 67 05 22</p>
            <a href="mailto:sale@m-weld.ru" class="text-base text-white">sale@m-weld.ru</a>
          </div>
               
        </div>
      </div>
    </div>

  </div>
</template>