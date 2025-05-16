<script setup>
  const currentData = new Date().getFullYear()

</script>


<template>
  <div class=" ">

    <div class="">
      <div class="container px-4 mx-auto">
        <div class="flex gap-16 items-end justify-between">

          <div class="grid grid-cols-1 gap-0.5">
            <p class="text-base text-white">г. Псков, ООО «Техносвар КС», 180006, ул Шоссейная д. 3,</p> 
            <p class="text-base text-white">тел. (8112) 72 52 13, факс: (8112) 67 05 22</p>
            <a href="mailto:sale@m-weld.ru" class="text-base text-white">sale@m-weld.ru</a>
          </div>

          <p class="text-base text-white">© {{ currentData }} Продажа сварочного оборудования	</p>

        </div>
      </div>
    </div>

  </div>
</template>