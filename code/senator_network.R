library(igraph)

#setwd("~/Dropbox/Work/current/stat222sp15-private/senators/")

senators = read.csv("senators.csv", header = TRUE)

# fmat[i, j] = 1 means senator j follows senator i
# i.e., row i has senator i's followers
fmat = as.matrix(read.csv("followersmatrix.csv", header = TRUE))

nfollowers = apply(fmat, 1, sum)
nfollowing = apply(fmat, 2, sum)

mat = matrix(1:4, ncol = 2, byrow = TRUE)
image(t(mat)[,2:1])
image_mat <- function(mat, ...){
  n = nrow(mat)
  image(t(mat)[,n:1], ...)
}

partyorder = order(senators$party, nfollowers, decreasing = TRUE)
fmat_reorder = fmat[partyorder, partyorder]
#red = row(fmat_reorder) <= 54
purple = row(fmat_reorder) >= 55 &row(fmat_reorder) <= 56
blue = row(fmat_reorder) >= 57
fmat_reorder[purple] = fmat_reorder[purple] * 2
fmat_reorder[blue] = fmat_reorder[blue] * 3

par(mar = c(5, 5, 1, 1), mgp = rep(1, 3))
image_mat(fmat_reorder, col = c("black", "red", "purple", "blue"),
          xlab = "Followers (same ordering as rows)",
      ylab = "Senators\n(ordered by party, # followers)",
      xaxt = "n", yaxt = "n")
abline(h = (100-54)/100, col = "white")
abline(h = (100-56)/100, col = "white")
abline(v = 54/100, col = "white")
abline(v = 56/100, col = "white")
dev.print(pdf, "presentation/followermat.pdf", height = 8, width = 8.5)

senators[nfollowing==99,]

pmat_nonzero = function(mat){
  mean(mat[row(mat)!=col(mat)] > 0)
}

pmat_nonzero(fmat_reorder[1:54, 1:54]) #[1] 0.6645702
pmat_nonzero(fmat_reorder[57:100, 57:100]) #[1] 0.5776956
mean(fmat_reorder[1:54, 57:100] > 0) #[1] 0.2390572
mean(fmat_reorder[57:100, 1:54] > 0) #[1] 0.2651515

names = paste(senators$first_name, senators$last_name)
graph3col = expand.grid(sen1 = names, sen2 = names)
graph3col$edge = c(fmat)
graph3col = graph3col[graph3col$edge == 1,]

senators_network = graph.data.frame(graph3col, directed=FALSE)

V(senators_network) #prints the list of vertices (people)
E(senators_network) #prints the list of edges (relationships)

#get_abb = function(x){
#  paste(substring(strsplit(x, split = " ")[[1]], 1, 1), collapse = "")
#}
#abbrev = sapply(V(senators_network)$name, get_abb)

index = match(V(senators_network)$name, names)
party_reorder = senators$party[index]
col = ifelse(party_reorder=="R", "red", "blue")
col[party_reorder=="I"] = "purple"
V(senators_network)$color =  col
V(senators_network)$size = log(senators$nfollowers[index], base = 5)

label = rep(NA, length(names))
#include = c("Alan Franken", "John McCain", "Cory Booker")
#for(name in include)
#  label[V(senators_network)$name == name] = get_abb(name)

V(senators_network)$label = label # NA is none
V(senators_network)$label.dist=1
E(senators_network)$width = 0.1

par(mai=rep(0, 4))
l = layout.fruchterman.reingold(senators_network, area=vcount(senators_network)^2.3, repulserad=vcount(senators_network)^5)
plot(senators_network, layout=l)
text(locator(1), "Franken", pos = 4)
text(locator(1), "McCain", pos = 2)
text(locator(1), "Booker", pos = 4)
dev.print(pdf, file = "presentation/network.pdf", height = 10, width = 10)

V(senators_network)$label = abbrev # NA is none
V(senators_network)$label.dist=0
plot(senators_network, layout=layout.fruchterman.reingold)
plot(senators_network, layout=layout.kamada.kawai)

#el = lapply(1:100, function(i){cbind(i, followers[[i]])})
#graph2col_full = do.call(rbind, el)
#senators_network_full = graph.data.frame(graph2col_full, directed=FALSE)
#is_sen = as.numeric(V(senators_network_full)$name) <= 100 
#V(senators_network_full)$size = ifelse(is_sen, 5, 0.1)
#E(senators_network_full)$width = 0.1
#V(senators_network_full)$label = NA

#par(mai=rep(0.5, 4))
#plot(senators_network_full)
