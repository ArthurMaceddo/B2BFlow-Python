# B2B - PROJECT

1st Commit Chore -
Base do projeto, principais arquivos

2st Commit feat -
O projeto se conecta ao banco de dados Supabase e busca os contatos na tabela contacts.
A consulta retorna os campos name e phone_number, que serão usados para personalizar e enviar as mensagens.

3st Commit
Juntei a parte que pega os contatos do banco com a parte que envia a mensagem do WhatsApp.
Adicionei um tratamento de erros para o caso de a Z-API dar algum erro, para que o código não pare de funcionar de repente.
Deixei a parte de envio da mensagem mais limpa e organizada.
