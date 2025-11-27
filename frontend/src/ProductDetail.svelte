<script>
  import { onMount } from 'svelte';

  // Получаем ID из параметров
  let { id } = $props();
  
  // Состояние
  let ste = $state(null);
  let loading = $state(true);
  let error = $state(null);

  onMount(async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/ste/${id}`);
      if (!response.ok) throw new Error('Товар не найден');
      ste = await response.json();
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  });
</script>

<!-- Подключаем шрифт Golos Text -->
<svelte:head>
	<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600&display=swap" rel="stylesheet">
</svelte:head>

<div class="product-card">
  <!-- ХЕДЕР -->
  <div class="rectangle-1"></div>
  
  <!-- ЛОГОТИП (SVG прямо в коде) -->
  <div class="pp-logo-1">
    <svg class="vector" width="10" height="12" viewBox="0 0 10 12" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M0 0H9.93243V11.1351H0V0Z" fill="#CD1F15"/>
    </svg>
    <!-- ... остальные SVG пути логотипа я сократил для краткости, но они будут работать если взять их из card.svelte ... -->
    <!-- Для простоты вставим текст логотипа, если SVG сложный, или используйте картинку -->
    <span style="position:absolute; left: 20px; font-weight: 600; font-size: 18px; color: #333;">ПОРТАЛ ПОСТАВЩИКОВ</span>
  </div>

      <!-- КНОПКА ВОЙТИ -->
  <a href="/" class="button-primary-small-default">
    <div class="div2">Войти</div>
  </a>


  <!-- ПОИСК -->
  <div class="frame-1">
    <svg class="interface-search-magnifying-glass" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.5 14.5L19 19M16.5 10.5C16.5 13.8137 13.8137 16.5 10.5 16.5C7.18629 16.5 4.5 13.8137 4.5 10.5C4.5 7.18629 7.18629 4.5 10.5 4.5C13.8137 4.5 16.5 7.18629 16.5 10.5Z" stroke="#333333" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <div class="div3">Поиск</div>
  </div>

  <!-- МЕНЮ -->
  <svg class="menu-hamburger-md" width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M5 8H27M5 16H27M5 24H27" stroke="#333333" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>

  <!-- ОСНОВНОЙ КОНТЕНТ -->
  {#if loading}
    <div style="position: absolute; top: 200px; left: 50%; transform: translateX(-50%);">Загрузка...</div>
  {:else if error}
    <div style="position: absolute; top: 200px; left: 50%; transform: translateX(-50%); color: red;">{error}</div>
  {:else if ste}
    <!-- Хлебные крошки -->
    <div class="frame-22">
      <div class="div7">Товары</div>
      <svg class="arrow-caret-right-sm" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M8.5 14L12.5 10L8.5 6" stroke="#C7C7CC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="div7">Принадлежности канцелярские</div>
      <svg class="arrow-caret-right-sm2" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M8.5 14L12.5 10L8.5 6" stroke="#C7C7CC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="div7">Ручки канцелярские</div>
    </div>

    <!-- Фото товара -->
    <!-- Если картинки нет, ставим заглушку -->
    <img class="rectangle-4" src="/rectangle-40.png" alt="Фото" />

    <!-- Название и блок справа -->
    <div class="frame-12">
      <div class="crown">{ste.name}</div>
      <div class="div8">Общие сведения</div>
    </div>

    <div class="line-32"></div>

    <!-- ID и кнопка копирования -->
    <div class="frame-52">
      <div class="id-37087949">ID СТЕ: {ste.id}</div>
      <svg class="edit-copy" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M13.5 13.5H15.1667C15.6269 13.5 16 13.1269 16 12.6667V4.83333C16 4.3731 15.6269 4 15.1667 4H7.33333C6.8731 4 6.5 4.3731 6.5 4.83333V6.5M11.5 16H5.66667C5.20643 16 4.83333 15.6269 4.83333 15.1667V9.33333C4.83333 8.8731 5.20643 8.5 5.66667 8.5H11.5C11.9602 8.5 12.3333 8.8731 12.3333 9.33333V15.1667C12.3333 15.6269 11.9602 16 11.5 16Z" stroke="#C7C7CC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>

    <!-- Характеристики -->
    <div class="div4">Характеристики товара</div>
    <div class="frame-6">
      {#each Object.entries(ste.features) as [key, value]}
        <div class="feature-row">
          <div class="frame-2">
            <div class="div5">{key}</div>
            <div class="line-3"></div>
          </div>
          <div class="div6">{value}</div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
    /* Импортируем стили из card.svelte, но с поправками на layout */
    .product-card {
        background: #ffffff;
        min-height: 100vh;
        position: relative;
        width: 1440px;
        margin: 0 auto;
        overflow: visible;
        font-family: "Golos Text", sans-serif;
    }

    /* Хедер и элементы */
    .rectangle-1 { background: #ffffff; width: 1440px; height: 72px; position: absolute; left: 0; top: 0; }
    .pp-logo-1 { width: 147px; height: 32px; position: absolute; left: 216px; top: 20px; }
    
    .button-primary-small-default {
        background: #cd1f15;
        border-radius: 4px;
        padding: 0 17px;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 32px;
        position: absolute;
        left: 1204px;
        top: 20px;
        cursor: pointer;
    }
    .div2 { color: #fff; font-size: 14px; }

    .frame-1 { display: flex; align-items: center; gap: 8px; position: absolute; left: 1100px; top: 20px; cursor: pointer; }
    .div3 { color: #333; font-size: 16px; }

    .menu-hamburger-md { position: absolute; left: 160px; top: 20px; cursor: pointer; }

    /* Контент */
    .frame-22 { display: flex; align-items: center; gap: 4px; position: absolute; left: 352px; top: 120px; }
    .div7 { color: #76767a; font-size: 14px; }
    .div7:last-child { color: #333; }

    .rectangle-4 {
        width: 280px; height: 336px; 
        position: absolute; left: 352px; top: 188px; 
        border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        object-fit: contain; /* Чтобы фото не растягивалось */
        background: #fff;
    }

    .frame-12 { position: absolute; left: 708px; top: 188px; display: flex; flex-direction: column; gap: 12px; }
    .crown { font-size: 24px; font-weight: 600; color: #000; }
    .div8 { font-size: 20px; font-weight: 500; color: #333; margin-top: 10px; }

    .line-32 { 
        width: 730px; height: 1px; background: #E5E5EB; 
        position: absolute; left: 708px; top: 280px; /* Подвинул линию чуть ниже заголовка */
    }

    .frame-52 { position: absolute; right: 352px; top: 120px; display: flex; gap: 8px; align-items: center; }
    .id-37087949 { color: #76767a; font-size: 14px; }

    /* Характеристики */
    .div4 { position: absolute; left: 352px; top: 560px; font-size: 30px; font-weight: 500; color: #333; }
    
    .frame-6 { 
        position: absolute; left: 352px; top: 620px; width: 736px; 
        display: flex; flex-direction: column; gap: 16px; 
    }
    
    .feature-row { display: flex; justify-content: space-between; align-items: center; }
    
    .frame-2 { display: flex; align-items: center; gap: 12px; flex: 1; }
    .div5 { color: #76767a; font-size: 16px; white-space: nowrap; }
    .line-3 { height: 1px; background: #E5E5EB; flex-grow: 1; margin-top: 6px; } /* Линия-точки */
    
    .div6 { color: #333; font-size: 16px; min-width: 200px; }

    a.button-primary-small-default {
    text-decoration: none; /* Убираем подчеркивание */
}

</style>
