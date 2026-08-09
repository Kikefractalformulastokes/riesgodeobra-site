/**
 * RiesgoDeObra — first-party conversion event tracking.
 *
 * No analytics provider is connected yet (no GA4/Plausible measurement ID
 * has been supplied). This file defines and fires the real conversion
 * events into window.dataLayer so that connecting GA4 (or GTM, or Plausible
 * via its goal/event API) later is a one-line change, not a rewrite.
 *
 * To activate: add the GA4 (or chosen provider) snippet before this script,
 * and it will pick up everything already pushed to dataLayer.
 */
(function () {
  window.dataLayer = window.dataLayer || [];

  function track(event, detail) {
    var payload = Object.assign({ event: event, page: location.pathname, ts: Date.now() }, detail || {});
    window.dataLayer.push(payload);
  }
  window.rdoTrack = track;

  document.addEventListener('DOMContentLoaded', function () {
    track('page_view');

    document.querySelectorAll('a[href*="buy.stripe.com"]').forEach(function (a) {
      a.addEventListener('click', function () {
        track('payment_link_click', { href: a.href, label: a.textContent.trim() });
      });
    });

    document.querySelectorAll('a[href*="tally.so"]').forEach(function (a) {
      a.addEventListener('click', function () {
        track('form_start', { href: a.href, label: a.textContent.trim() });
      });
    });

    document.querySelectorAll('a[href^="mailto:"]').forEach(function (a) {
      a.addEventListener('click', function () { track('email_click', { href: a.href }); });
    });

    document.querySelectorAll('a[href^="tel:"]').forEach(function (a) {
      a.addEventListener('click', function () { track('telephone_click', { href: a.href }); });
    });

    var heroCta = document.querySelector('.hero .btn-primary');
    if (heroCta) heroCta.addEventListener('click', function () { track('hero_cta_click', { label: heroCta.textContent.trim() }); });

    var ejemploLink = document.querySelector('a[href="/ejemplo-informe/"]');
    if (ejemploLink) ejemploLink.addEventListener('click', function () { track('report_example_view'); });

    document.querySelectorAll('.card.svc a, .demo-card a').forEach(function (a) {
      a.addEventListener('click', function () { track('service_cta_click', { href: a.href, label: a.textContent.trim() }); });
    });
  });
})();
