document.addEventListener("DOMContentLoaded", function() {
          const movimentacoes=document.querySelectorAll("li[data-status");
          movimentacoes.forEach(li=>{
                    const status=li.getAttribute('data-status').toLowerCase()
                    if (status==='recebida'){
                              const form=li.querySelector('form');
                              if (form){
                                        form.style.display='none';
                                        
                              }
                    }
          })




});