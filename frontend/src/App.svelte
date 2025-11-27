<script>
  import ProductDetail from './ProductDetail.svelte';
  import Login from './Login.svelte'; // Ваша главная страница
  
  // Svelte 5: реактивное состояние URL
  let path = $state(window.location.pathname);

  // Обработка кнопок "Назад/Вперед" в браузере
  function handlePopState() {
    path = window.location.pathname;
  }

  // Перехват кликов по ссылкам, чтобы страница не перезагружалась
  function handleLinkClick(e) {
    const anchor = e.target.closest('a');
    // Если клик по ссылке на наш же сайт
    if (anchor && anchor.href.startsWith(window.location.origin)) {
      e.preventDefault();
      window.history.pushState({}, '', anchor.href);
      path = anchor.pathname;
    }
  }
</script>

<svelte:window onpopstate={handlePopState} onclick={handleLinkClick} />

<main>
  {#if path === '/'}
    <Login />
  {:else if path.startsWith('/sku/')}
    <!-- Парсим ID из URL вручную: /sku/123 -> 123 -->
    {@const id = path.split('/')[2]}
    <ProductDetail {id} />
  {:else}
    <h1>404: Страница не найдена</h1>
    <a href="/">На главную</a>
  {/if}
</main>
